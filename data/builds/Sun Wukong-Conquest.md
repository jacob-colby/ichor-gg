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
    - name: Umbral Link
      pick_rate: 0.05
      win_rate: 0.74
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.57
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
  last_verified: '2026-11-03'
  god_win_rate: 0.5356725146198831
  god_matches_won: 458
  god_matches_played: 855
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Runeforged Hammer, Kinetic Cuirass, Genji''s Guard, Tekko-Kagi,
    The Crusher, Avenging Blade, Hydra''s Lament, Titan''s Bane, Lernaean Bow, Oni
    Hunter''s Garb, Breastplate of Valor, Erosion, Pharaoh''s Curse, Eye of Providence,
    Wyrmskin Hide, Eros'' Bow, Midgardian Mail, Draconic Scale, Golden Blade, Death
    Metal, Bragi''s Harp, Shogun''s Ofuda, Shield of the Phoenix, Obsidian Shard,
    Helm of Radiance, Leviathan''s Hide, Dominance, Arondight, Triton''s Conch, Spear
    of Desolation, Nimble Ring, Heartseeker, Jade Scepter, Helm of Darkness, Shifter''s
    Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Kinetic Cuirass,
    Shield Splitter, Shield of the Phoenix, Jotunn''s Revenge, Runeforged Hammer,
    Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Soul Gem, Ethereal Staff, Erosion,
    Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Avenging Blade, Breastplate
    of Valor, Tekko-Kagi, Midgardian Mail, Hydra''s Lament, Pharaoh''s Curse, Titan''s
    Bane, Wyrmskin Hide, Chandra''s Grace, Leviathan''s Hide, Rod of Asclepius, Shogun''s
    Ofuda, Lernaean Bow, Blood-Bound Book, Helm of Radiance, Stone of Binding, Helm
    of Darkness, Sphere of Negation, Eros'' Bow, Soul Locket, Magi''s Cloak, Shifter''s
    Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    The Reaper:
      total: 0.56
      efficiency: 0.51
      win: 0.63
      pick: 0.17
      fit: 0.57
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.84
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
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Tekko-Kagi, Titan''s Bane, Avenging Blade, Obsidian Shard, Amanita Charm, Spear
    of Desolation, Stone of Binding, Soul Gem, Heartseeker, Runeforged Hammer, Shield
    Splitter, Spear of the Magus, Genji''s Guard, Screeching Gargoyle, Kinetic Cuirass,
    Void Stone, Void Shield, Doom Orb, Hydra''s Lament, The World Stone, Breastplate
    of Valor, Avatar''s Parashu, Oni Hunter''s Garb, Dreamer''s Idol, Lernaean Bow,
    Pendulum Blade, Helm of Radiance, Midgardian Mail, Erosion, Eros'' Bow, Death
    Metal, Pharaoh''s Curse, Eye of Providence, Nimble Ring, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.54
      win: 0.61
      pick: 0.17
      fit: 0.63
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.02
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.39
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
    Eros'' Bow, Soul Gem, Pharaoh''s Curse, Riptalon, Shogun''s Ofuda, Breastplate
    of Valor, Hydra''s Lament, Dominance, Oni Hunter''s Garb, Bragi''s Harp, Obsidian
    Shard, Titan''s Bane, Helm of Radiance, Avenging Blade, Blood-Bound Book, Midgardian
    Mail, Spear of Desolation, Qin''s Blade, Bracer of The Abyss, Erosion, Eye of
    Providence, Leviathan''s Hide, Vital Amplifier, Ancient Signet.'
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
  - Spear of Desolation
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Spear of Desolation,
    Hydra''s Lament, Amanita Charm, Soul Gem, Shield of the Phoenix, Lotus Sickle,
    Screeching Gargoyle, Chronos'' Pendant, Kinetic Cuirass, Arondight, Runeforged
    Hammer, Shield Splitter, Gem of Focus, Heartwood Charm, Obsidian Shard, Helm of
    Radiance, Gladiator''s Shield, Chandra''s Grace, Eye of Erebus, Oni Hunter''s
    Garb, Eros'' Bow, Nimble Ring, Prophetic Cloak, Tekko-Kagi, Ancient Signet, Jade
    Scepter, Midgardian Mail, Titan''s Bane, Erosion, Damaru, Avenging Blade, Helm
    of Darkness, Regrowth Striders, Pharaoh''s Curse, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.55
      pick: 0.22
      fit: 0.52
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Shield Splitter, Runeforged Hammer, Kinetic Cuirass, Genji''s Guard,
    Tekko-Kagi, Avenging Blade, Hydra''s Lament, Titan''s Bane, Lernaean Bow, Oni
    Hunter''s Garb, Breastplate of Valor, Erosion, Pharaoh''s Curse, Eye of Providence,
    Wyrmskin Hide, Eros'' Bow, Midgardian Mail, Draconic Scale, Golden Blade, Death
    Metal, Bragi''s Harp, Shogun''s Ofuda, Shield of the Phoenix, The Crusher, Obsidian
    Shard, Helm of Radiance, Leviathan''s Hide, Dominance, Arondight, Triton''s Conch,
    Spear of Desolation, Nimble Ring, Shifter''s Shield, Heartseeker, Jade Scepter,
    Helm of Darkness.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
