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
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Gluttonous Grimoire
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Jotunn''s Revenge, Genji''s Guard, Shield Splitter, Golden Blade, Runeforged Hammer,
    Tyrfing, The Crusher, Soul Gem, Oni Hunter''s Garb, Hydra''s Lament, Shield of
    the Phoenix, Draconic Scale, Breastplate of Valor, Avenging Blade, Death Metal,
    Bragi''s Harp, Nimble Ring, Blood-Bound Book, Erosion, Eye of Providence, Midgardian
    Mail, Spear of Desolation, Leviathan''s Hide, Wyrmskin Hide, Lernaean Bow, Dominance,
    Heartseeker, Hide of the Nemean Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s
    Curse, Triton''s Conch, Helm of Radiance, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.58
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
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Rod of Tahuti, Soul Gem, Blood-Bound Book, Shield Splitter, Genji''s Guard, Jotunn''s
    Revenge, Phoenix Feather, Yogi''s Necklace, Runeforged Hammer, Ethereal Staff,
    Golden Blade, Draconic Scale, Tyrfing, Oni Hunter''s Garb, Erosion, Eye of Providence,
    Bloodforge, Bancroft''s Talon, Breastplate of Valor, Chandra''s Grace, Riptalon,
    Midgardian Mail, Hydra''s Lament, Leviathan''s Hide, Hide of the Nemean Lion,
    Avenging Blade, Regrowth Striders, Shogun''s Ofuda, Wyrmskin Hide, Pharaoh''s
    Curse, Death Metal, Nimble Ring, Stone of Binding, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.18
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.59
    Shield Splitter:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Reaper:
      total: 0.59
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.79
  community_ordered:
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, The Crusher,
    Soul Gem, Amanita Charm, Kinetic Cuirass, Avenging Blade, Spear of Desolation,
    Genji''s Guard, Heartseeker, Screeching Gargoyle, Stone of Binding, Tekko-Kagi,
    Titan''s Bane, Obsidian Shard, Void Stone, Void Shield, Shield Splitter, Runeforged
    Hammer, Toxic Blade, Tyrfing, Spear of the Magus, Golden Blade, Dreamer''s Idol,
    Silverbranch Bow, Breastplate of Valor, Oni Hunter''s Garb, Riptalon, Hydra''s
    Lament, Shield of the Phoenix, Avatar''s Parashu, Doom Orb, Blood-Bound Book,
    Draconic Scale, Death Metal, Nimble Ring, The World Stone.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.51
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.17
      fit: 0.66
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.62
      pick: 0.02
      fit: 0.59
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
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
  - Kinetic Cuirass
  - Tyrfing
  - Gluttonous Grimoire
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Golden Blade,
    Kinetic Cuirass, Genji''s Guard, Jotunn''s Revenge, Nimble Ring, Soul Gem, Toxic
    Blade, Shield Splitter, Runeforged Hammer, Bragi''s Harp, Breastplate of Valor,
    Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse, Lernaean Bow, Dominance,
    Silverbranch Bow, Shield of the Phoenix, Riptalon, Tekko-Kagi, Blood-Bound Book,
    Hydra''s Lament, Draconic Scale, Qin''s Blade, Spear of Desolation, Midgardian
    Mail, Bracer of The Abyss, Erosion, Death Metal, Ancient Signet, Leviathan''s
    Hide, Eye of Providence, Helm of Radiance, Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.63
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.58
      win: 0.61
      pick: 0.17
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.29
  community_ordered:
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
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s
    Revenge, Soul Gem, Berserker''s Shield, Breastplate of Valor, Amanita Charm, Spear
    of Desolation, Shield of the Phoenix, Kinetic Cuirass, Hydra''s Lament, Screeching
    Gargoyle, Chronos'' Pendant, Arondight, Gladiator''s Shield, Shield Splitter,
    Blood-Bound Book, Runeforged Hammer, Gem of Focus, Heartwood Charm, Tyrfing, Oni
    Hunter''s Garb, Chandra''s Grace, Nimble Ring, Golden Blade, Eye of Erebus, Ancient
    Signet, Helm of Radiance, Draconic Scale, Prophetic Cloak, Damaru, Death Metal,
    Midgardian Mail, Polynomicon, Regrowth Striders, Erosion, Obsidian Shard, Jade
    Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.4
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
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
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.45
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.22
      fit: 0.48
    Soul Gem:
      total: 0.56
      efficiency: 0.58
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
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Jotunn''s Revenge, Genji''s Guard, Shield Splitter, Golden Blade, Runeforged
    Hammer, Tyrfing, Soul Gem, Oni Hunter''s Garb, Hydra''s Lament, Shield of the
    Phoenix, Draconic Scale, Breastplate of Valor, Avenging Blade, Death Metal, Bragi''s
    Harp, Nimble Ring, Blood-Bound Book, Erosion, Eye of Providence, Midgardian Mail,
    The Crusher, Shifter''s Shield, Spear of Desolation, Leviathan''s Hide, Wyrmskin
    Hide, Lernaean Bow, Dominance, Heartseeker, Hide of the Nemean Lion, Tekko-Kagi,
    Shogun''s Ofuda, Pharaoh''s Curse, Triton''s Conch, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.57
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.33
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
