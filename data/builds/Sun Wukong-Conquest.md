---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.68
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.57
    - name: The Crusher
      pick_rate: 0.02
      win_rate: 0.62
  - name: Sanguine Lash
    pick_rate: 0.39
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.46
    - name: Jotunn's Revenge
      pick_rate: 0.07
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.63
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.53
  - name: Gluttonous Grimoire
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.55
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.49
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.61
    - name: Sundering Echo
      pick_rate: 0.07
      win_rate: 0.64
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.58
    - name: Umbral Link
      pick_rate: 0.05
      win_rate: 0.74
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.4
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.42
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-11-04'
  god_win_rate: 0.5362149532710281
  god_matches_won: 459
  god_matches_played: 856
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Runeforged Hammer
  - Gluttonous Grimoire
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm,
    Shield Splitter, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Nimble Ring,
    Genji''s Guard, Soul Gem, The Crusher, Tyrfing, Tekko-Kagi, Hydra''s Lament, Avenging
    Blade, Titan''s Bane, Lernaean Bow, Oni Hunter''s Garb, Breastplate of Valor,
    Erosion, Pharaoh''s Curse, Eye of Providence, Midgardian Mail, Obsidian Shard,
    Death Metal, Wyrmskin Hide, Helm of Radiance, Draconic Scale, Toxic Blade, Blood-Bound
    Book, Shield of the Phoenix, Leviathan''s Hide, Bragi''s Harp, Shogun''s Ofuda,
    Dominance, Arondight, Spear of Desolation.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.61
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.33
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.17
      fit: 0.5
  community_ordered:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Soul Gem, Kinetic
    Cuirass, Shield of the Phoenix, Shield Splitter, Jotunn''s Revenge, Blood-Bound
    Book, Runeforged Hammer, Genji''s Guard, Golden Blade, Phoenix Feather, Yogi''s
    Necklace, Bloodforge, Ethereal Staff, Nimble Ring, Riptalon, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Breastplate of Valor, Draconic Scale, Avenging Blade,
    Hydra''s Lament, Bancroft''s Talon, Tekko-Kagi, Tyrfing, Midgardian Mail, Pharaoh''s
    Curse, Chandra''s Grace, Titan''s Bane, Leviathan''s Hide, Helm of Radiance, Lernaean
    Bow, Sphere of Negation, Wyrmskin Hide, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.28
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.59
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Reaper:
      total: 0.58
      efficiency: 0.56
      win: 0.63
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Tekko-Kagi
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Soul Gem,
    The Crusher, Tekko-Kagi, Avenging Blade, Titan''s Bane, Obsidian Shard, Amanita
    Charm, Spear of Desolation, Stone of Binding, Runeforged Hammer, Genji''s Guard,
    Screeching Gargoyle, Toxic Blade, Shield Splitter, Heartseeker, Spear of the Magus,
    Kinetic Cuirass, Void Stone, Void Shield, Nimble Ring, Silverbranch Bow, Golden
    Blade, Riptalon, Doom Orb, Hydra''s Lament, The World Stone, Breastplate of Valor,
    Tyrfing, Oni Hunter''s Garb, Lernaean Bow, Dreamer''s Idol, Avatar''s Parashu,
    Helm of Radiance, Blood-Bound Book, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.61
      pick: 0.17
      fit: 0.66
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.62
      pick: 0.02
      fit: 0.59
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Golden Blade, Nimble Ring, Amanita
    Charm, Jotunn''s Revenge, Tyrfing, Genji''s Guard, Tekko-Kagi, Kinetic Cuirass,
    Toxic Blade, Runeforged Hammer, Shield Splitter, Lernaean Bow, Silverbranch Bow,
    Soul Gem, Pharaoh''s Curse, Riptalon, Shogun''s Ofuda, Breastplate of Valor, Hydra''s
    Lament, Dominance, Oni Hunter''s Garb, Bragi''s Harp, Obsidian Shard, Titan''s
    Bane, Helm of Radiance, Avenging Blade, Blood-Bound Book, Midgardian Mail, Spear
    of Desolation, Qin''s Blade, Bracer of The Abyss, Erosion, Eye of Providence,
    Leviathan''s Hide, Vital Amplifier, Ancient Signet.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.19
    Nimble Ring:
      total: 0.53
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.17
      fit: 0.38
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.08
  community_ordered:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Soul Gem, Breastplate of Valor, Spear of
    Desolation, Hydra''s Lament, Amanita Charm, Shield of the Phoenix, Nimble Ring,
    Screeching Gargoyle, Chronos'' Pendant, Kinetic Cuirass, Arondight, Runeforged
    Hammer, Shield Splitter, Obsidian Shard, Gem of Focus, Golden Blade, Heartwood
    Charm, Helm of Radiance, Blood-Bound Book, Oni Hunter''s Garb, Chandra''s Grace,
    Eye of Erebus, Gladiator''s Shield, Ancient Signet, Prophetic Cloak, Tekko-Kagi,
    Tyrfing, Jade Scepter, Midgardian Mail, Titan''s Bane, Spear of the Magus, Avenging
    Blade, Erosion, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.4
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.45
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.22
      fit: 0.48
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Shield Splitter, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Nimble
    Ring, Genji''s Guard, Soul Gem, Tyrfing, Tekko-Kagi, Hydra''s Lament, Avenging
    Blade, Titan''s Bane, Lernaean Bow, Oni Hunter''s Garb, Breastplate of Valor,
    Erosion, Pharaoh''s Curse, Eye of Providence, Midgardian Mail, Obsidian Shard,
    Death Metal, Wyrmskin Hide, Helm of Radiance, Draconic Scale, Toxic Blade, Blood-Bound
    Book, The Crusher, Shield of the Phoenix, Leviathan''s Hide, Bragi''s Harp, Shogun''s
    Ofuda, Dominance, Arondight, Spear of Desolation.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.61
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.33
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
