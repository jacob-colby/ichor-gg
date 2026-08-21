---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.58
  slot_order:
  - name: Tyrfing
    pick_rate: 0.65
    win_rate: 0.55
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.05
      win_rate: 0.72
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.62
  - name: Odysseus' Bow
    pick_rate: 0.51
    win_rate: 0.56
    alternates:
    - name: Dominance
      pick_rate: 0.07
      win_rate: 0.44
    - name: Hastened Fatalis
      pick_rate: 0.05
      win_rate: 0.51
  - name: Hastened Fatalis
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.61
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.43
  - name: The Executioner
    pick_rate: 0.21
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.18
      win_rate: 0.59
    - name: Silverbranch Bow
      pick_rate: 0.17
      win_rate: 0.58
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.68
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.6
  - name: Qin's Blade
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.56
    - name: Bow
      pick_rate: 0.09
      win_rate: 0.66
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.54
    win_rate: 0.62
  - name: Death's Toll
    pick_rate: 0.21
    win_rate: 0.44
  - name: Conduit Gem
    pick_rate: 0.04
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-21'
  god_win_rate: 0.5707376058041113
  god_matches_won: 472
  god_matches_played: 827
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Berserker''s Shield, Jotunn''s Revenge, Lernaean Bow,
    Demon Blade, Deathbringer, Damaru, Tekko-Kagi, The Crusher, Runeforged Hammer,
    Musashi''s Dual Swords, Pharaoh''s Curse, The Reaper, Toxic Blade, Hydra''s Lament,
    Shogun''s Ofuda, Genji''s Guard, Amanita Charm, Breastplate of Valor, Rage, Kinetic
    Cuirass, Heartseeker, Shield Splitter, Sun Beam Bow, Avenging Blade, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.73
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.83
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.65
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.52
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Berserker''s Shield, The Crusher, Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Golden Blade, Lernaean Bow, Heartseeker, The Reaper, Transcendence,
    Runeforged Hammer, Tekko-Kagi, Amanita Charm, Freya''s Tears, Deathbringer, Damaru,
    Kinetic Cuirass, Titan''s Bane, Shield Splitter, Pharaoh''s Curse, Toxic Blade,
    Arondight, Eye of Providence, Avenging Blade, Musashi''s Dual Swords, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.62
      pick: 0.05
      fit: 0.24
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.53
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Berserker''s Shield, Jotunn''s Revenge, Lernaean Bow,
    Demon Blade, Deathbringer, Damaru, Musashi''s Dual Swords, Tekko-Kagi, The Crusher,
    Runeforged Hammer, The Reaper, Pharaoh''s Curse, Hydra''s Lament, Toxic Blade,
    Rage, Shogun''s Ofuda, Genji''s Guard, Amanita Charm, Breastplate of Valor, Kinetic
    Cuirass, Heartseeker, Shield Splitter, Avenging Blade, Sun Beam Bow, Dominance.'
  slot_scores:
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.79
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.61
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.49
    Damaru:
      total: 0.52
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.52
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Golden Blade, Jotunn''s Revenge, The Reaper, Pharaoh''s Curse, Shogun''s Ofuda,
    Runeforged Hammer, Shifter''s Shield, Freya''s Tears, Phoenix Feather, Yogi''s
    Necklace, Genji''s Guard, Shield Splitter, Breastplate of Valor, Lernaean Bow,
    Spectral Armor, Mantle Of Discord, Stone of Binding, Eye of the Storm, Chandra''s
    Grace, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide, The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.54
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.69
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Tekko-Kagi, Berserker''s
    Shield, Heartseeker, Toxic Blade, Golden Blade, Avenging Blade, Titan''s Bane,
    Stone of Binding, Lernaean Bow, Screeching Gargoyle, Runeforged Hammer, Deathbringer,
    Damaru, Genji''s Guard, Avatar''s Parashu, Amanita Charm, Breastplate of Valor,
    Kinetic Cuirass, Pharaoh''s Curse, Hydra''s Lament, Void Shield, Demon Blade,
    Void Stone, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.58
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.77
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.69
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Golden Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Jotunn''s Revenge, Lernaean Bow,
    Demon Blade, Tekko-Kagi, Deathbringer, Damaru, The Crusher, Pharaoh''s Curse,
    Runeforged Hammer, Toxic Blade, Shogun''s Ofuda, The Reaper, Genji''s Guard, Amanita
    Charm, Hydra''s Lament, Breastplate of Valor, Kinetic Cuirass, Musashi''s Dual
    Swords, Heartseeker, Sun Beam Bow, Shield Splitter, Eye of Providence, Freya''s
    Tears, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.16
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.75
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.59
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Berserker''s Shield, Hydra''s Lament, Freya''s Tears, Shield
    of the Phoenix, Golden Blade, Lernaean Bow, Screeching Gargoyle, Arondight, The
    Crusher, Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Pharaoh''s Curse,
    Deathbringer, Damaru, Chandra''s Grace, The Reaper, Shogun''s Ofuda, Tekko-Kagi,
    Eye of Providence, Eye of Erebus, Toxic Blade, Demon Blade, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.21
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.52
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The Cosmic Horror
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, The Cosmic
    Horror, Nimble Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of Desolation,
    Berserker''s Shield, Spear of the Magus, Obsidian Shard, The Crusher, Genji''s
    Guard, Bragi''s Harp, Breastplate of Valor, Golden Blade, Bracer of The Abyss,
    Chronos'' Pendant, The Reaper, Helm of Radiance, Lernaean Bow, Hydra''s Lament,
    Doom Orb, Tekko-Kagi, The World Stone, Ancient Signet, Freya''s Tears, Ethereal
    Staff, Heartseeker, Rod of Asclepius, Runeforged Hammer, Blood-Bound Book, Dreamer''s
    Idol, Amanita Charm, Kinetic Cuirass, Toxic Blade, Gem of Focus, Bancroft''s Talon,
    Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.53
      win: 0.72
      pick: 0.05
      fit: 0.35
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The Cosmic Horror
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, The Cosmic Horror,
    Jotunn''s Revenge, Death Metal, Nimble Ring, Gluttonous Grimoire, Soul Gem, Berserker''s
    Shield, The Crusher, Spear of the Magus, Golden Blade, Obsidian Shard, Bragi''s
    Harp, The Reaper, Lernaean Bow, Tekko-Kagi, Spear of Desolation, Heartseeker,
    Runeforged Hammer, Bracer of The Abyss, Helm of Radiance, Doom Orb, Deathbringer,
    Damaru, Hydra''s Lament, The World Stone, Toxic Blade, Titan''s Bane, Genji''s
    Guard, Amanita Charm, Ancient Signet, Breastplate of Valor, Dreamer''s Idol, Ethereal
    Staff, Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Pharaoh''s Curse,
    Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.34
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.57
    The Cosmic Horror:
      total: 0.56
      efficiency: 0.53
      win: 0.72
      pick: 0.05
      fit: 0.34
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.47
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  flex_slots:
  - Lernaean Bow
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Golden Blade, Berserker''s Shield, Jotunn''s Revenge,
    Lernaean Bow, Demon Blade, Deathbringer, Damaru, Dominance, Tekko-Kagi, The Crusher,
    Runeforged Hammer, Musashi''s Dual Swords, Pharaoh''s Curse, The Reaper, Toxic
    Blade, Hydra''s Lament, Shogun''s Ofuda, Genji''s Guard, Amanita Charm, Breastplate
    of Valor, Rage, Kinetic Cuirass, Heartseeker, Shield Splitter, Sun Beam Bow, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.83
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.3
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  flex_slots:
  - Lernaean Bow
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Golden Blade, Berserker''s Shield,
    Jotunn''s Revenge, Lernaean Bow, Demon Blade, Deathbringer, Damaru, Dominance,
    Tekko-Kagi, The Crusher, Runeforged Hammer, Musashi''s Dual Swords, Pharaoh''s
    Curse, The Reaper, Toxic Blade, Hydra''s Lament, Shogun''s Ofuda, Genji''s Guard,
    Amanita Charm, Breastplate of Valor, Rage, Kinetic Cuirass, Heartseeker, Shield
    Splitter, Sun Beam Bow, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.73
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.55
      pick: 0.65
      fit: 0.83
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.68
      pick: 0.39
      fit: 0.52
  swaps:
  - added: Silverbranch Bow
    removed: Riptalon
    reason: community 68% win over 149 matches (vs 57% on this god), taking the model's
      weakest slot from Riptalon
  starter: *id001
---
