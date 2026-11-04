---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Golden Blade
    pick_rate: 0.32
    win_rate: 0.66
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.65
    - name: Berserker's Shield
      pick_rate: 0.2
      win_rate: 0.68
  - name: Berserker's Shield
    pick_rate: 0.3
    win_rate: 0.62
    alternates:
    - name: Golden Blade
      pick_rate: 0.4
      win_rate: 0.66
    - name: Shogun's Ofuda
      pick_rate: 0.11
      win_rate: 0.63
  - name: Kinetic Cuirass
    pick_rate: 0.27
    win_rate: 0.65
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.28
      win_rate: 0.64
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.66
  - name: Shogun's Ofuda
    pick_rate: 0.17
    win_rate: 0.64
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.18
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.71
    - name: Hussar's Wings
      pick_rate: 0.09
      win_rate: 0.68
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Hussar's Wings
      pick_rate: 0.08
      win_rate: 0.76
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.39
    win_rate: 0.65
  - name: Death's Embrace
    pick_rate: 0.24
    win_rate: 0.74
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-11-04'
  god_win_rate: 0.6300236406619385
  god_matches_won: 533
  god_matches_played: 846
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
  - Jotunn's Revenge
  - Berserker's Shield
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s Revenge, Genji''s
    Guard, Gluttonous Grimoire, Breastplate of Valor, Runeforged Hammer, Soul Gem,
    Erosion, Hydra''s Lament, Eye of Providence, Oni Hunter''s Garb, Draconic Scale,
    Shield of the Phoenix, Stone of Binding, The Reaper, Helm of Darkness, Helm of
    Radiance, Midgardian Mail, Magi''s Cloak, Screeching Gargoyle, Titan''s Bane,
    Mantle Of Discord, Avenging Blade, Spear of Desolation, Leviathan''s Hide, Wyrmskin
    Hide, Obsidian Shard, Arondight, Ancile, Blood-Bound Book, Hide of the Nemean
    Lion, Death Metal, Stampede, Void Stone, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.34
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.33
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.55
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.48
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, The Reaper,
    Jotunn''s Revenge, Shield Splitter, Genji''s Guard, Gluttonous Grimoire, Blood-Bound
    Book, Runeforged Hammer, Phoenix Feather, Yogi''s Necklace, Bloodforge, Breastplate
    of Valor, Ethereal Staff, Hydra''s Lament, Chandra''s Grace, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Draconic Scale, Bancroft''s Talon, Avenging Blade,
    Midgardian Mail, Regrowth Striders, Glorious Pridwen, Titan''s Bane, Helm of Radiance,
    Leviathan''s Hide, Spear of Desolation, Sphere of Negation, Stone of Binding,
    Wyrmskin Hide, Helm of Darkness, Screeching Gargoyle, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.35
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.34
    Freya's Tears:
      total: 0.58
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.42
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.59
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.65
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem,
    Amanita Charm, Stone of Binding, Genji''s Guard, Screeching Gargoyle, Avenging
    Blade, The Reaper, Shield Splitter, Spear of Desolation, Titan''s Bane, Obsidian
    Shard, Void Stone, Void Shield, Breastplate of Valor, The Crusher, Runeforged
    Hammer, Spear of the Magus, Heartseeker, Hydra''s Lament, Oni Hunter''s Garb,
    Erosion, Helm of Radiance, Eye of Providence, Doom Orb, Shield of the Phoenix,
    Draconic Scale, The World Stone, Midgardian Mail, Tekko-Kagi, Helm of Darkness,
    Magi''s Cloak, Leviathan''s Hide, Mantle Of Discord, Dreamer''s Idol, Blood-Bound
    Book.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.25
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.65
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Jotunn''s Revenge, Nimble
    Ring, Shield Splitter, Gluttonous Grimoire, Tyrfing, Breastplate of Valor, Soul
    Gem, Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse, Lernaean Bow, Toxic Blade,
    Hydra''s Lament, Oni Hunter''s Garb, Silverbranch Bow, Helm of Radiance, Erosion,
    Eye of Providence, Stone of Binding, Spear of Desolation, Shield of the Phoenix,
    Obsidian Shard, Draconic Scale, Midgardian Mail, Helm of Darkness, Screeching
    Gargoyle, The Reaper, Magi''s Cloak, Titan''s Bane, Riptalon, Leviathan''s Hide,
    Mantle Of Discord, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.66
      pick: 0.32
      fit: 0.53
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.62
      pick: 0.41
      fit: 0.43
    Nimble Ring:
      total: 0.56
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.46
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Soul Gem, Amanita Charm, Breastplate of Valor, Spear of Desolation, Gluttonous
    Grimoire, Hydra''s Lament, Shield of the Phoenix, Shield Splitter, Screeching
    Gargoyle, Chronos'' Pendant, Arondight, Helm of Radiance, Runeforged Hammer, Prophetic
    Cloak, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye of Providence, Obsidian
    Shard, Draconic Scale, Stone of Binding, Gladiator''s Shield, Gem of Focus, Midgardian
    Mail, Blood-Bound Book, Magi''s Cloak, Heartwood Charm, Mantle Of Discord, Leviathan''s
    Hide, The Reaper, Ancient Signet, Regrowth Striders, Chandra''s Grace, Eye of
    Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.51
    Freya's Tears:
      total: 0.6
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.59
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire, Soul
    Gem, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Spear of Desolation, Obsidian
    Shard, Shield Splitter, Helm of Radiance, Breastplate of Valor, Helm of Darkness,
    Spear of the Magus, Runeforged Hammer, Blood-Bound Book, The Reaper, Hydra''s
    Lament, Titan''s Bane, Ancient Signet, Death Metal, Chronos'' Pendant, Oni Hunter''s
    Garb, Jade Scepter, Doom Orb, Shield of the Phoenix, Erosion, The World Stone,
    Eye of Providence, Screeching Gargoyle, Stone of Binding, Draconic Scale, Midgardian
    Mail, The Crusher, Magi''s Cloak, Dreamer''s Idol, Arondight, Avenging Blade,
    Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.24
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Genji''s Guard, Shield Splitter, Spear
    of Desolation, Obsidian Shard, Helm of Radiance, Runeforged Hammer, Breastplate
    of Valor, The Reaper, Titan''s Bane, Helm of Darkness, Spear of the Magus, Hydra''s
    Lament, Blood-Bound Book, Death Metal, Oni Hunter''s Garb, Ancient Signet, Erosion,
    Eye of Providence, The Crusher, Jade Scepter, Stone of Binding, Doom Orb, Shield
    of the Phoenix, Draconic Scale, Midgardian Mail, Chronos'' Pendant, Avenging Blade,
    The World Stone, Magi''s Cloak, Screeching Gargoyle, Heartseeker, Arondight, Leviathan''s
    Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.25
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.24
      fit: 0.36
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.65
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
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
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Shield Splitter, Jotunn''s
    Revenge, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor, Runeforged
    Hammer, Soul Gem, Erosion, Hydra''s Lament, Eye of Providence, Oni Hunter''s Garb,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, The Reaper, Helm of Darkness,
    Helm of Radiance, Midgardian Mail, Magi''s Cloak, Screeching Gargoyle, Titan''s
    Bane, Mantle Of Discord, Avenging Blade, Spear of Desolation, Leviathan''s Hide,
    Wyrmskin Hide, Obsidian Shard, Arondight, Ancile, Blood-Bound Book, Hide of the
    Nemean Lion, Death Metal, Stampede, Void Stone, Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.65
      pick: 0.0
      fit: 0.29
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.41
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.65
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.65
      pick: 0.42
      fit: 0.61
    Shield Splitter:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
---
