---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.47
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.59
    alternates:
    - name: Transcendence
      pick_rate: 0.31
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.57
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.56
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.56
  - name: Hydra's Lament
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.55
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.58
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.64
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.67
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.4
    win_rate: 0.64
  - name: Bumba's Cudgel
    pick_rate: 0.27
    win_rate: 0.49
  - name: Archmage's Gem
    pick_rate: 0.1
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-21'
  god_win_rate: 0.5634674922600619
  god_matches_won: 546
  god_matches_played: 969
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, The Crusher, Berserker''s Shield, Nimble
    Ring, Tyrfing, Golden Blade, Tekko-Kagi, Lernaean Bow, Silverbranch Bow, Gluttonous
    Grimoire, The Reaper, Soul Gem, Riptalon, Spear of the Magus, Runeforged Hammer,
    Bragi''s Harp, Spear of Desolation, Obsidian Shard, Toxic Blade, Dominance, Genji''s
    Guard, Deathbringer, Damaru, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Pharaoh''s Curse, Demon Blade, Bracer of The Abyss, Shield Splitter, Freya''s
    Tears, Musashi''s Dual Swords, Doom Orb, Avenging Blade, The Cosmic Horror, Shogun''s
    Ofuda, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.43
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.59
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation,
    The Crusher, Spear of the Magus, Berserker''s Shield, Genji''s Guard, Obsidian
    Shard, Breastplate of Valor, Bragi''s Harp, Lernaean Bow, The Reaper, Tyrfing,
    Doom Orb, Golden Blade, Runeforged Hammer, Ancient Signet, Tekko-Kagi, The World
    Stone, Helm of Radiance, Chronos'' Pendant, Silverbranch Bow, The Cosmic Horror,
    Bracer of The Abyss, Dominance, Freya''s Tears, Amanita Charm, Ethereal Staff,
    Riptalon, Rod of Asclepius, Wish-Granting Pearl, Kinetic Cuirass, Dreamer''s Idol,
    Deathbringer.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.26
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.48
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.26
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Soul Gem, Gluttonous Grimoire, Spear of Desolation, Death
    Metal, Nimble Ring, The Crusher, Spear of the Magus, Obsidian Shard, Berserker''s
    Shield, The Reaper, Genji''s Guard, Breastplate of Valor, Silverbranch Bow, Tekko-Kagi,
    Riptalon, Doom Orb, Lernaean Bow, Tyrfing, The Cosmic Horror, Golden Blade, Freya''s
    Tears, Bragi''s Harp, The World Stone, Chronos'' Pendant, Runeforged Hammer, Dreamer''s
    Idol, Helm of Radiance, Amanita Charm, Toxic Blade, Bracer of The Abyss, Kinetic
    Cuirass, Pendulum Blade, Ancient Signet, Ethereal Staff, Shield of the Phoenix,
    Rod of Asclepius, Arondight.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.15
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.51
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.15
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.61
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Death Metal
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, The Reaper, Riptalon, Ethereal Staff, Rod of Asclepius,
    Gluttonous Grimoire, Death Metal, Golden Blade, Runeforged Hammer, Nimble Ring,
    Freya''s Tears, The Crusher, Pharaoh''s Curse, Genji''s Guard, Breastplate of
    Valor, Phoenix Feather, Shifter''s Shield, Yogi''s Necklace, Shield Splitter,
    Shogun''s Ofuda, Chandra''s Grace, Eye of the Storm, Mantle Of Discord, Spectral
    Armor, Stone of Binding, Blood-Bound Book, Lernaean Bow, Tyrfing, Erosion, Spear
    of the Magus, Silverbranch Bow, Lifebinder, Eye of Providence, Toxic Blade, Leviathan''s
    Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.58
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Soul Gem, Silverbranch
    Bow, The Reaper, Tekko-Kagi, Spear of the Magus, Riptalon, Death Metal, Obsidian
    Shard, Spear of Desolation, Berserker''s Shield, Nimble Ring, Avenging Blade,
    Toxic Blade, Stone of Binding, Tyrfing, Lernaean Bow, Golden Blade, Doom Orb,
    The Cosmic Horror, Screeching Gargoyle, The World Stone, Runeforged Hammer, Dreamer''s
    Idol, Avatar''s Parashu, Genji''s Guard, Breastplate of Valor, Pendulum Blade,
    Bragi''s Harp, Amanita Charm, Kinetic Cuirass, Void Shield, Deathbringer, Damaru,
    Dominance, Freya''s Tears.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.05
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.55
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.17
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.62
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.72
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Berserker''s Shield, Riptalon, Tyrfing,
    Silverbranch Bow, Golden Blade, Gluttonous Grimoire, Death Metal, Soul Gem, The
    Crusher, Lernaean Bow, The Reaper, Tekko-Kagi, Toxic Blade, Spear of the Magus,
    Bragi''s Harp, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Obsidian
    Shard, Spear of Desolation, Pharaoh''s Curse, Dominance, Amanita Charm, Bracer
    of The Abyss, Kinetic Cuirass, Qin''s Blade, Shogun''s Ofuda, Freya''s Tears,
    Deathbringer, Damaru, Helm of Radiance, Eye of Providence, Demon Blade, Shield
    Splitter, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.3
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.66
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Spear of
    Desolation, Genji''s Guard, Breastplate of Valor, Nimble Ring, Freya''s Tears,
    Berserker''s Shield, Death Metal, Gluttonous Grimoire, Chronos'' Pendant, The
    Crusher, Shield of the Phoenix, Spear of the Magus, Screeching Gargoyle, Obsidian
    Shard, Silverbranch Bow, Arondight, Gem of Focus, Tyrfing, Lernaean Bow, Riptalon,
    Golden Blade, The Reaper, Totem of Death, Amanita Charm, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Kinetic Cuirass, Bragi''s Harp, Helm of Radiance, Bracer of
    The Abyss, Chandra''s Grace, Doom Orb, The Cosmic Horror, Toxic Blade, Pharaoh''s
    Curse, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.09
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.54
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.09
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.22
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard,
    Berserker''s Shield, The Crusher, Bragi''s Harp, Genji''s Guard, Breastplate of
    Valor, Chronos'' Pendant, The Reaper, Helm of Radiance, Doom Orb, The Cosmic Horror,
    Silverbranch Bow, Tyrfing, Lernaean Bow, Bracer of The Abyss, Golden Blade, Tekko-Kagi,
    The World Stone, Riptalon, Ancient Signet, Runeforged Hammer, Ethereal Staff,
    Dreamer''s Idol, Freya''s Tears, Rod of Asclepius, Amanita Charm, Gem of Focus,
    Kinetic Cuirass, Jade Scepter, Wish-Granting Pearl, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.42
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Soul Gem, The Crusher, Spear of the Magus, Berserker''s
    Shield, Obsidian Shard, Spear of Desolation, Bragi''s Harp, The Reaper, Tyrfing,
    Tekko-Kagi, Lernaean Bow, Golden Blade, Silverbranch Bow, Runeforged Hammer, Riptalon,
    Doom Orb, The Cosmic Horror, Helm of Radiance, Bracer of The Abyss, The World
    Stone, Genji''s Guard, Breastplate of Valor, Dreamer''s Idol, Ancient Signet,
    Ethereal Staff, Rod of Asclepius, Amanita Charm, Deathbringer, Damaru, Dominance,
    Chronos'' Pendant, Kinetic Cuirass, Toxic Blade, Shield Splitter.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.4
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.2
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, The Crusher, Berserker''s
    Shield, Nimble Ring, Tyrfing, Golden Blade, Tekko-Kagi, Lernaean Bow, Silverbranch
    Bow, Gluttonous Grimoire, Soul Gem, Riptalon, The Reaper, Spear of the Magus,
    Runeforged Hammer, Bragi''s Harp, Spear of Desolation, Obsidian Shard, Toxic Blade,
    Dominance, Genji''s Guard, Deathbringer, Damaru, Breastplate of Valor, Amanita
    Charm, Kinetic Cuirass, Pharaoh''s Curse, Demon Blade, Bracer of The Abyss, Shield
    Splitter, Freya''s Tears, Musashi''s Dual Swords, Doom Orb, Avenging Blade, The
    Cosmic Horror, Shogun''s Ofuda, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.43
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.23
  starter: *id001
---
