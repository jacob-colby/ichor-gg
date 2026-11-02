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
    pick_rate: 0.15
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
    win_rate: 0.62
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
    win_rate: 0.4
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
  last_verified: '2026-11-02'
  god_win_rate: 0.5375586854460094
  god_matches_won: 458
  god_matches_played: 852
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sundering Echo
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Runeforged Hammer, Shield Splitter, Genji''s Guard, Tekko-Kagi,
    The Crusher, Hydra''s Lament, Titan''s Bane, Avenging Blade, Lernaean Bow, Breastplate
    of Valor, Oni Hunter''s Garb, Pharaoh''s Curse, Erosion, Wyrmskin Hide, Eye of
    Providence, Draconic Scale, Midgardian Mail, Golden Blade, Eros'' Bow, Shogun''s
    Ofuda, Shield of the Phoenix, Obsidian Shard, Leviathan''s Hide, Bragi''s Harp,
    Death Metal, Heartseeker, Dominance, Nimble Ring, Helm of Radiance, Triton''s
    Conch, Spear of Desolation, Ancile, Arondight, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.55
    Sundering Echo:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.15
      fit: 0.33
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Sundering Echo
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sundering Echo
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Sundering Echo
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Kinetic Cuirass,
    Shield of the Phoenix, Jotunn''s Revenge, Shield Splitter, Phoenix Feather, Runeforged
    Hammer, Genji''s Guard, Yogi''s Necklace, Soul Gem, Ethereal Staff, Erosion, Eye
    of Providence, Draconic Scale, Oni Hunter''s Garb, Breastplate of Valor, Chandra''s
    Grace, Pharaoh''s Curse, Midgardian Mail, Tekko-Kagi, Avenging Blade, Hydra''s
    Lament, Wyrmskin Hide, Shogun''s Ofuda, Titan''s Bane, Leviathan''s Hide, Rod
    of Asclepius, Stone of Binding, Blood-Bound Book, Lernaean Bow, Sphere of Negation,
    Helm of Darkness, Eros'' Bow, Ancile, Glorious Pridwen, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.64
    Sundering Echo:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.15
      fit: 0.27
    The Reaper:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.17
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Jotunn's Revenge
  - Sundering Echo
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, The Crusher,
    Tekko-Kagi, Titan''s Bane, Obsidian Shard, Avenging Blade, Amanita Charm, Spear
    of Desolation, Heartseeker, Soul Gem, Stone of Binding, Screeching Gargoyle, Kinetic
    Cuirass, Genji''s Guard, Void Stone, Spear of the Magus, Void Shield, Runeforged
    Hammer, Shield Splitter, Doom Orb, The World Stone, Breastplate of Valor, Hydra''s
    Lament, Oni Hunter''s Garb, Dreamer''s Idol, Lernaean Bow, Pendulum Blade, Avatar''s
    Parashu, Midgardian Mail, Pharaoh''s Curse, Erosion, Nimble Ring, Helm of Radiance,
    Eros'' Bow, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.17
      fit: 0.63
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.53
      efficiency: 0.45
      win: 0.62
      pick: 0.02
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.81
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
    this god: Berserker''s Shield, Rod of Tahuti, Golden Blade, Nimble Ring, Jotunn''s
    Revenge, Amanita Charm, Tyrfing, Genji''s Guard, Toxic Blade, Kinetic Cuirass,
    Tekko-Kagi, Silverbranch Bow, Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer,
    Riptalon, Soul Gem, Eros'' Bow, Shield Splitter, Shogun''s Ofuda, Breastplate
    of Valor, Obsidian Shard, Dominance, Oni Hunter''s Garb, Hydra''s Lament, Bragi''s
    Harp, Titan''s Bane, Qin''s Blade, Midgardian Mail, Blood-Bound Book, Erosion,
    Bracer of The Abyss, Helm of Radiance, Spear of Desolation, Avenging Blade, Leviathan''s
    Hide, Shield of the Phoenix, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.19
    Nimble Ring:
      total: 0.52
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.56
      win: 0.62
      pick: 0.17
      fit: 0.38
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.81
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Spear of Desolation,
    Amanita Charm, Hydra''s Lament, Soul Gem, Shield of the Phoenix, Screeching Gargoyle,
    Chronos'' Pendant, Kinetic Cuirass, Arondight, Heartwood Charm, Runeforged Hammer,
    Gem of Focus, Chandra''s Grace, Obsidian Shard, Shield Splitter, Gladiator''s
    Shield, Prophetic Cloak, Nimble Ring, Eye of Erebus, Oni Hunter''s Garb, Helm
    of Radiance, Eros'' Bow, Midgardian Mail, Pharaoh''s Curse, Erosion, Tekko-Kagi,
    Titan''s Bane, Totem of Death, Regrowth Striders, Jade Scepter, Eye of Providence,
    Leviathan''s Hide, Helm of Darkness, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.55
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.23
      fit: 0.52
    Spear of Desolation:
      total: 0.53
      efficiency: 0.56
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
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Runeforged Hammer, Shield Splitter, Genji''s Guard,
    Tekko-Kagi, Hydra''s Lament, Titan''s Bane, Avenging Blade, Lernaean Bow, Breastplate
    of Valor, Oni Hunter''s Garb, Pharaoh''s Curse, Erosion, Wyrmskin Hide, Eye of
    Providence, Draconic Scale, Midgardian Mail, Golden Blade, Eros'' Bow, Shogun''s
    Ofuda, Shield of the Phoenix, Obsidian Shard, Leviathan''s Hide, Bragi''s Harp,
    Death Metal, Heartseeker, Dominance, Nimble Ring, Shifter''s Shield, The Crusher,
    Helm of Radiance, Triton''s Conch, Spear of Desolation, Ancile, Arondight.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.7
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
